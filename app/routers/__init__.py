__all__ = [
	'router', 
]

from typing import Annotated
from fastapi import APIRouter

from .products import router as product_router
from .users import router as user_router
from .orders import router as order_router
from .reviews import router as review_router



router = APIRouter(prefix='/api/v1')
router.include_router(product_router)
router.include_router(user_router)
router.include_router(order_router)
router.include_router(review_router)