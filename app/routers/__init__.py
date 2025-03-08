__all__ = ['router']


from fastapi import APIRouter
from .products import router as product_router
from .users import router as user_router

router = APIRouter(prefix='/api/v1')
router.include_router(product_router)
router.include_router(user_router)
