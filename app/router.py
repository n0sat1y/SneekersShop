from fastapi import APIRouter, Depends


from services import *
from schemas import ProductSchema
from core.batabase import SessionDep
from repositories import ProductRepository

router = APIRouter()


@router.get("/products", response_model=list[ProductSchema])
async def get_products(session: SessionDep) -> list[ProductSchema]:
	# result = await ProductServices().get_products()
	result = await ProductRepository.get_products(session)
	return result

@router.get("/products/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, session: SessionDep) -> ProductSchema:
	# result = await ProductServices().get_product(product_id)
	result = await ProductRepository.get_product(session, product_id)

	return result