
from django.contrib import auth
from owslib.wms import WebMapService
from owslib.wmts import WebMapTileService

import hashlib

# Pantalla inicial
def principal_view(request):
    template = 'QVCataleg/mapaInicial.html'
    llistaMapes = RefMapaWMS.objects.all()
    llistaMapesCompostos = RefMapa.objects.all()
    for mapa in llistaMapes:
        mapa.mapa_actual = False
        mapa.save()
    llistaApps = Aplicacio.objects.all()
    context = {'llistaAplicacions' : llistaApps, 'llistaMapes' : llistaMapes, 'llistaMapesCompostos' : llistaMapesCompostos}
    return render(request, template, context)

# View per mostrar el mapa
def mostraMapa(request, mapa, tip):
    if (tip==1):
        mapesBasics = True
    else:
        mapesBasics = False
    llistaTotalMapes = RefMapaWMS.objects.all()
    llistaMapesCompostos = RefMapa.objects.all()
    llista = Aplicacio.objects.all()
    template = 'QVCataleg/gestioWMS.html'
    if (mapesBasics):
        mapes = ['BAS', 'SAT', 'PLANOLBCN', 'GUIA_PLANOL', 'PLANOLBCN_WEB']
        mapaFons = mapes[mapa]
        context = {'mapaFons' : mapaFons, 'mapesBasics' : True, 'llistaAplicacions' : llista, 'llistaMapes' : llistaMapes, 'llistaMapesCompostos' : llistaMapesCompostos}
    else:
        llistaCapes = []
        llistaMapes = [[]]
        mapaFons = RefMapaWMS.objects.get(id=mapa)
        mapaFons.mapa_actual = True
        mapaFons.save()

        mapes = RefMapaWMS.objects.filter(mapa_actual=True).order_by('nom')
        for mapa in mapes:
            pUrl = mapa.pUrl
            matrixSet = mapa.matrixSet
            tipus = mapa.tipus
            format = mapa.format
            llistaCapes = []
            if mapa.tipus == 'wms':
                wms = WebMapService(pUrl, version='1.1.1')
                for content in wms.contents:
                    llistaCapes.append([content, normalitzaCapa(content,mapa.id)])
            elif mapa.tipus == 'wmts':
                wms = WebMapTileService(pUrl)
                for content in wms.contents:
                    llistaCapes.append([content, normalitzaCapa(content,mapa.id)])
            elif mapa.tipus == 'vector':
                wms = ''
                llistaCapes.append([mapa.nom,normalitzaCapa(mapa.nom,mapa.id)])

            llistaMapes.append([wms,tipus,pUrl,matrixSet,format,llistaCapes])

        context = {'llistaMapes2' : llistaMapes, 'mapesBasics' : False, 'llistaAplicacions' : llista, 'llistaMapes' : llistaTotalMapes, 'llistaMapesCompostos' : llistaMapesCompostos}
        #context = {'wms' : wms, 'tipus' : tipus, 'pUrl' : pUrl, 'urlCapabilities' :urlCapabilities, 'matrixSet' : matrixSet, 'format': format, 'llistaCapes' : llistaCapes, 'mapesBasics' : False, 'llistaAplicacions' : llista, 'llistaMapes' : llistaMapes}

    return render(request, template, context)

def mostraMapaCompost(request, mapa):

    template = 'QVCataleg/gestioMapa.html'
    llistaMapes = RefMapaWMS.objects.all()
    llistaMapesCompostos = RefMapa.objects.all()
    llista = Aplicacio.objects.all()

    mapaCompost=RefMapa.objects.get(id=mapa)
    llistaCodisCapes = RefMapaCapa.objects.filter(codiMapa=mapaCompost.codiMapa)
    capes=[]
    for codi in llistaCodisCapes:
        capa = RefCapa.objects.get(codiCapa=codi.codiCapa)
        capes.append(capa)

    context = {'mapa': mapaCompost, 'llistaCapes': capes, 'mapesBasics' : False, 'llistaAplicacions' : llista, 'llistaMapes' : llistaMapes, 'llistaMapesCompostos' : llistaMapesCompostos}

    return render(request, template, context)

# Catàleg de mapes
def catalegDinamic_view(request):
    llistaAplis = Aplicacio.objects.all()
    refMapes = RefMapaWMS.objects.all()
    llistaMapesCompostos = RefMapa.objects.all()
    template = 'QVCataleg/catalegDinamic.html'
    if request.method == 'POST':
        if 'formOne' in request.POST:
            form = CatalegForm(request.POST)
            if form.is_valid():
                refMapes = RefMapaWMS.objects.filter(nom__contains=form.cleaned_data['nomCercat'])
                numTrobats = len(refMapes)
        if 'formTwo' in request.POST:
            form = CatalegForm(request.POST)
            if form.is_valid():
                llistaMapesCompostos = RefMapa.objects.filter(nomMapa__contains=form.cleaned_data['nomCercat'])
    else:
        form = CatalegForm()
    
    context = {'llistaMapes' : refMapes, 
                'numMapes' : len(refMapes),
                'form' : form,
                'llistaAplicacions' : llistaAplis,
                'llistaMapesCompostos': llistaMapesCompostos}

    return render(request, template, context)


# Catàleg de capes
def catalegDinamicCapes_view(request):
    llistaAplis = Aplicacio.objects.all()
    refMapes = RefMapaWMS.objects.all()
    llistaMapesCompostos = RefMapa.objects.all()
    capes = RefCapa.objects.all()
    template = 'QVCataleg/catalegDinamicCapes.html'
    if request.method == 'POST':
        if 'formOne' in request.POST:
            form = CatalegForm(request.POST)
            if form.is_valid():
                capes = RefCapa.objects.filter(nomCapa__contains=form.cleaned_data['nomCercat'])
        elif 'formTwo' in request.POST:
            id_list = request.POST.getlist('boxes')
            nomMapa = request.POST.get('nom')
            metaMapa = request.POST.get('metaMapa')
            print(id_list)
            codi = abs(hash(nomMapa)) % (10 ** 5)
            print(codi)
            mapaCompost = RefMapa(codiMapa=codi, nomMapa=nomMapa, metaMapa=metaMapa)
            mapaCompost.save()
            for x in id_list:
                capa = RefCapa.objects.get(id=int(x))
                print(capa.codiCapa)
                mapaCapa = RefMapaCapa(codiMapa=codi, codiCapa=capa.codiCapa)
                mapaCapa.save()
            form = CatalegForm()
            mapaCompost = RefMapa.objects.last()
            return redirect(mostraMapaCompost,mapa=mapaCompost.id)
    else:
        form = CatalegForm()

    context = {'llistaMapes' : refMapes,
                'form' : form,
                'llistaAplicacions' : llistaAplis,
                'llistaMapesCompostos': llistaMapesCompostos,
                'llistaCapes': capes}

    return render(request, template, context)

def pokemon_view(request):
    pokemons = Pokemon.objects.all()
    template = 'QVCataleg/pokemon.html'
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            p = Pokemon(nom=form.cleaned_data['nom'], tipus=form.cleaned_data['tipus'],foto=form.cleaned_data['foto'])
            print(p.nom,p.tipus)
            p.save()
    else:
        form = PokemonForm()

    context = {
                'form' : form,
                'pokemons' : pokemons}


    return render(request, template, context)

def test_view(request):
    template = 'QVCataleg/index.html'

    context = {}


    return render(request, template, context)

def mapaForm_view(request, tipus):
    print(tipus)
    mapes = RefMapaWMS.objects.all()
    llistaMapesCompostos = RefMapa.objects.all()
    template = 'QVCataleg/refMapaWMSForm.html'
    if request.method == 'POST':
        if tipus == 'wms':
            form = RefMapaWMSForm(request.POST, request.FILES)
        elif tipus == 'wmts':
            form = RefMapaWMTSForm(request.POST, request.FILES)
        elif tipus == 'vector':
            form = RefMapaVectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mapa = RefMapaWMS.objects.last()
            mapa.urlCapabilities = mapa.pUrl + '?request=GetCapabilities&service=WMS'
            mapa.save()
            # s'afegeix a les BBDD les capes del mapa que s'acaba de donar d'alta
            if tipus == 'wms':
                wms = WebMapService(mapa.pUrl, version='1.1.1')
                for content in wms.contents:
                    codi = normalitzaCapa(content, mapa.id)
                    capa = RefCapa(codiCapa=codi, nomCapa=content, url=mapa.pUrl, tipus=mapa.tipus, matrixSet=mapa.matrixSet)
                    capa.save()
            elif tipus == 'wmts':
                wms = WebMapTileService(mapa.pUrl)
                for content in wms.contents:
                    codi = normalitzaCapa(content, mapa.id)
                    capa = RefCapa(codiCapa=codi, nomCapa=content, url=mapa.pUrl, tipus=mapa.tipus, matrixSet=mapa.matrixSet)
                    capa.save()
            elif tipus == 'vector':
                codi = normalitzaCapa(mapa.nom, mapa.id)
                capa = RefCapa(codiCapa=codi, nomCapa=mapa.nom, url=mapa.pUrl, tipus=mapa.tipus, matrixSet=mapa.matrixSet, format=mapa.format)
                capa.save()
            return redirect(catalegDinamic_view)

    else:
        if tipus == 'wms':
            form = RefMapaWMSForm(initial={'tipus': tipus})
        elif tipus == 'wmts':
            form = RefMapaWMTSForm(initial={'tipus': tipus})
        elif tipus == 'vector':
            form = RefMapaVectorForm(initial={'tipus': tipus})
    
    edita = False
    context = {
                'form' : form,
                'llistaMapes' : mapes,
                'edita': edita,
                'tipus': tipus,
                'llistaMapesCompostos': llistaMapesCompostos}


    return render(request, template, context)

    
def editaMapaForm_view(request, mapa):
    mapes = RefMapaWMS.objects.all()
    llistaMapesCompostos = RefMapa.objects.all()
    template = 'QVCataleg/refMapaWMSForm.html'
    m = RefMapaWMS.objects.get(pk=int(mapa))
    if request.method == 'POST':
        if m.tipus == 'wms':
            form = RefMapaWMSForm(request.POST, request.FILES, instance=m)
        elif m.tipus == 'wmts':
            form = RefMapaWMTSForm(request.POST, request.FILES, instance=m)
        elif m.tipus == 'vector':
            form = RefMapaVectorForm(request.POST, request.FILES, instance=m)
        if form.is_valid():
            form.save()
            m.urlCapabilities = m.pUrl + '?request=GetCapabilities&service=WMS'
            m.save()
            return redirect(catalegDinamic_view)

    else:
        if m.tipus == 'wms':
            form = RefMapaWMSForm(initial={'tipus': m.tipus}, instance=m)
        elif m.tipus == 'wmts':
            form = RefMapaWMTSForm(initial={'tipus': m.tipus}, instance=m)
        elif m.tipus == 'vector':
            form = RefMapaVectorForm(initial={'tipus': m.tipus}, instance=m)

    edita = True
    context = {
                'form' : form,
                'llistaMapes' : mapes,
                'edita': edita,
                'tipus': m.tipus,
                'llistaMapesCompostos': llistaMapesCompostos}


    return render(request, template, context)

def esborraMapaForm_view(request, mapa):
    mapa = RefMapaWMS.objects.get(pk=int(mapa))
    if mapa.tipus == 'wms':
        wms = WebMapService(mapa.pUrl, version='1.1.1')
        for content in wms.contents:
            codi = normalitzaCapa(content, mapa.id)
            capa = RefCapa.objects.get(codiCapa=codi)
            capa.delete()
    elif mapa.tipus == 'wmts':
        wms = WebMapTileService(mapa.pUrl)
        for content in wms.contents:
            codi = normalitzaCapa(content, mapa.id)
            capa = RefCapa.objects.get(codiCapa=codi)
            capa.delete()
    elif mapa.tipus == 'vector':
        codi = normalitzaCapa(mapa.nom, mapa.id)
        capa = RefCapa.objects.get(codiCapa=codi)
        capa.delete()
    if mapa.foto:
        mapa.foto.delete()
    mapa.delete()
    return redirect(catalegDinamic_view)

def esborraMapaCompostForm_view(request, mapa):
    mapa = RefMapa.objects.get(pk=int(mapa))
    capes = RefMapaCapa.objects.filter(codiMapa=mapa.codiMapa)
    for capa in capes:
        print(capa.codiCapa)
        capa.delete()
    mapa.delete()
    return redirect(catalegDinamic_view)


def normalitzaCapa(content,id):
    content = content.replace('-','_')
    content = content.replace(' ','_')
    content = str(content+'_'+str(id))
    return content