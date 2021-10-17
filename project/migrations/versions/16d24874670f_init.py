"""init

Revision ID: 16d24874670f
Revises: 
Create Date: 2021-10-17 00:38:50.089719

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             # NEW


# revision identifiers, used by Alembic.
revision = '16d24874670f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('modelo', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('placa', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ano', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_car_ano'), 'car', ['ano'], unique=False)
    op.create_index(op.f('ix_car_id'), 'car', ['id'], unique=False)
    op.create_index(op.f('ix_car_modelo'), 'car', ['modelo'], unique=False)
    op.create_index(op.f('ix_car_placa'), 'car', ['placa'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_car_placa'), table_name='car')
    op.drop_index(op.f('ix_car_modelo'), table_name='car')
    op.drop_index(op.f('ix_car_id'), table_name='car')
    op.drop_index(op.f('ix_car_ano'), table_name='car')
    op.drop_table('car')
    # ### end Alembic commands ###
