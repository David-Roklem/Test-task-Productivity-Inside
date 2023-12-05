"""alter table ads adding cascade="all, delete" for the related object to be removed from DB

Revision ID: 4e9719d32adb
Revises: 8858a46b855f
Create Date: 2023-12-05 10:24:37.297740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e9719d32adb'
down_revision: Union[str, None] = '8858a46b855f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'ads', ['id'])
    op.create_unique_constraint(None, 'comments', ['id'])
    op.create_unique_constraint(None, 'complaints', ['id'])
    op.create_unique_constraint(None, 'reviews', ['id'])
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'reviews', type_='unique')
    op.drop_constraint(None, 'complaints', type_='unique')
    op.drop_constraint(None, 'comments', type_='unique')
    op.drop_constraint(None, 'ads', type_='unique')
    # ### end Alembic commands ###