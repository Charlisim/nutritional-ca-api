"""fix back reference to food for ingredients

Revision ID: 361ab5352108
Revises: 2f89b42d2f5a
Create Date: 2021-11-02 12:20:50.733835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '361ab5352108'
down_revision = '2f89b42d2f5a'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
