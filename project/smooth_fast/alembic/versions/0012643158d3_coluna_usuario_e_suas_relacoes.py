"""COluna Usuario e suas relacoes

Revision ID: 0012643158d3
Revises: 6bd4698820a8
Create Date: 2022-12-29 02:19:21.947259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0012643158d3'
down_revision = '6bd4698820a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Usuario',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.Column('telefone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    with op.batch_alter_table('Usuario', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Usuario_ID'), ['ID'], unique=False)

    with op.batch_alter_table('Produto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_usuario_id', 'Usuario', ['usuario_id'], ['ID'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Produto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_usuario_id', type_='foreignkey')
        batch_op.drop_column('usuario_id')

    with op.batch_alter_table('Usuario', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Usuario_ID'))

    op.drop_table('Usuario')
    # ### end Alembic commands ###
