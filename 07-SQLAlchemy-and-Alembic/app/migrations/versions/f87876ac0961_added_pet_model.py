"""Added Pet model

Revision ID: f87876ac0961
Revises: 
Create Date: 2023-06-02 14:28:19.413947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f87876ac0961'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.Column('breed', sa.String(), nullable=True),
    sa.Column('temperament', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
