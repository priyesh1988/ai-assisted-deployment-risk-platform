
from sqlalchemy import text

def set_tenant_schema(db, tenant_id):
    db.execute(text(f"SET search_path TO tenant_{tenant_id}"))
