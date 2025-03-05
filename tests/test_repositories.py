import pytest


from app.repositories import ProductRepository


@pytest.mark.asyncio
async def test_get_products(session):
	res = await ProductRepository.get_products(session)
	assert res == []
	assert 1 == 1