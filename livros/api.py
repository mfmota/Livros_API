from ninja import Router,Query 
from .schemas import LivrosSchema,AvaliacaoSchema,FiltrosSortearSchema,LivrosViewSchema,LivrosIdSchema
from .models import Livros,Categorias
from typing import List

livros_router = Router()

@livros_router.get('/',response={200:List[LivrosViewSchema]})
def get_livro(request):
    livros=Livros.objects.all()
    return livros

@livros_router.post('/')
def create_livro(request, livro_schema:LivrosSchema):
    nome = livro_schema.dict()['nome']
    streaming = livro_schema.dict()['streaming']
    categorias = livro_schema.dict()['categorias']
    if streaming not in ['F','AK']:
        return 400,{'status': 'Erro:Streaming inválido'}
    livro = Livros(
        nome=nome,
        streaming=streaming,
    )
    livro.save()

    for categoria in categorias:
        categoria_temp = Categorias.objects.get(id=categoria)
        livro.categorias.add(categoria_temp)

    return{'status':'ok'}

@livros_router.put('/{livro_id}')
def avaliar_livro(request, livro_id:int, avaliacao_schema:AvaliacaoSchema):
    comentarios = avaliacao_schema.dict()['comentarios']
    nota = avaliacao_schema.dict()['nota']
    if nota < 0 or nota > 5:
        return 400,{'status':'Nota invalida'}
    try:
        livro = Livros.objects.get(id=livro_id)
        livro.comentarios=comentarios
        livro.nota=nota
        livro.save()

        return 200, {'status':'Avaliação realizada'}
    except:
        return 500,{'status':'Erro: Erro ao avaliar'}
    

@livros_router.delete('/{livro_id}')
def deletar_livro(request,livro_id:int):
    livro = Livros.objects.get(id=livro_id)
    livro.delete()

    return livro_id

@livros_router.get('/id/{livro_id}', response={200: LivrosIdSchema, 404: dict})
def get_livro(request, livro_id: int):
    try:
        livro = Livros.objects.get(id=livro_id)
        return livro
    except Livros.DoesNotExist:
        return 404, {"error": "Livro não encontrado"}

@livros_router.get('/sortear/', response={200: LivrosSchema, 404:dict})
def sortear_livro(request,filtros: Query[FiltrosSortearSchema]):
    nota_minima = filtros.dict()['nota_minima']
    categoria = filtros.dict()['categorias']
    reler = filtros.dict()['reler']

    livros = Livros.objects.all()

    if not reler:
        livros = livros.filter(nota=None)
    if nota_minima:
        livros = livros.filter(nota__gte=nota_minima)
    if categoria:
        livros = livros.filter(Categorias__id=categoria)    

    livro = livros.order_by('?').first()

    if livros.count() > 0:
        return 200, livro
    else:
        return 404,{'status':'Livro não encontrado'}