from graphene_django import DjangoObjectType
import graphene
from .models import Caja

class CajaType(DjangoObjectType):
    class Meta:
        model=Caja



class Query(graphene.ObjectType):
    cajas = graphene.List(CajaType)
    
    def resolve_cajas(self,info):
        return Caja.objects.all()
    
    
class CrearCaja(graphene.Mutation):
    
    
    class Arguments:
        monto= graphene.Float()
        tipo =graphene.String()
        fecha =graphene.DateTime()
        
    
    caja =graphene.Field(CajaType)
    
    def mutate(self,info,monto,tipo,fecha=None):
        
        caja=Caja(monto=monto,tipo=tipo,fecha=fecha)
        
        caja.save()
        
        return CrearCaja(caja=caja)
    
class EliminarCaja(graphene.Mutation):
    
    class Arguments:
        id =graphene.ID(required=True)
        
    estado =graphene.Boolean()
        
    def mutate(self,info,id):
        try:
            caja=Caja.objects.get(id=id)
            caja.delete()
            estado=True
        except Caja.DoesNotExist:
            estado=False
        return EliminarCaja(estado=estado)

class Mutaciones(graphene.ObjectType):
    crear_caja=CrearCaja.Field()
    eliminar_caja=EliminarCaja.Field()

schema = graphene.Schema(query=Query,mutation=Mutaciones)