import pytest

from app.schemas import ProductCreateSchema
from app.repositories import ProductRepository

@pytest.mark.asyncio
async def test_create_product(session):
	product = ProductCreateSchema(
		name='Test Product', 
		description='Some desc', 
		colors=['red', 'blue'], 
		category='snnekers',
		gender='man',
		sizes=[42, 43, 44],
		price=100
	)
	res = await ProductRepository.create_product(session, product)

	assert res is not None
	assert res.id is not None

@pytest.mark.asyncio
async def test_get_product(session):
	res = await ProductRepository.get_product(session, 1)
	assert res is not None