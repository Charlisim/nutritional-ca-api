"""fix back reference to food for ingredients 5

Revision ID: 836c15e12768
Revises: de5548a163a0
Create Date: 2021-11-02 12:34:51.514064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836c15e12768'
down_revision = 'de5548a163a0'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
