from fastapi import APIRouter

router = APIRouter()


@router.get("/api/produtos")
def list_products(repository):
    return repository.list_all()