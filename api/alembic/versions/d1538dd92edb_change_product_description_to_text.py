"""change Product.description to Text

Revision ID: d1538dd92edb
Revises: d677d0c69f7d
Create Date: 2024-05-14 16:33:30.234290

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d1538dd92edb"
down_revision: Union[str, None] = "d677d0c69f7d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "product",
        "description",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "product",
        "description",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
