"""Add ad_number field for Ad class which represents unique public number for an Ad

Revision ID: 63125e2acf26
Revises: 1728a05a41d2
Create Date: 2023-12-04 18:02:58.132483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63125e2acf26'
down_revision: Union[str, None] = '1728a05a41d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ads', sa.Column('ad_number', sa.BigInteger(), nullable=False))
    op.create_index(op.f('ix_ads_ad_number'), 'ads', ['ad_number'], unique=True)
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
    op.drop_index(op.f('ix_ads_ad_number'), table_name='ads')
    op.drop_column('ads', 'ad_number')
    # ### end Alembic commands ###
