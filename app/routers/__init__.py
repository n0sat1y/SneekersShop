__all__ = [
	'router', 
]

from typing import Annotated
from fastapi import APIRouter

from app.routers.products import router as product_router
from app.routers.users import router as user_router
from app.routers.orders import router as order_router
from app.routers.reviews import router as review_router



router = APIRouter(prefix='/api/v1')
router.include_router(product_router)
router.include_router(user_router)
router.include_router(order_router)
router.include_router(review_router)