from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database.database import get_session
from database.models import RoloReport


class ReportRepository:

    def salvar(self, dados):
        with get_session() as session:

            try:

                relatorio = session.scalar(
                    select(RoloReport).where(
                        RoloReport.numero_rolo == dados["numero_rolo"]
                    )
                )

                if relatorio is None:
                    relatorio = RoloReport()
                    session.add(relatorio)

                for campo, valor in dados.items():
                    setattr(relatorio, campo, valor)

                session.commit()

                return relatorio

            except SQLAlchemyError:
                session.rollback()
                raise

    def listar(self):
        with get_session() as session:
            return session.scalars(
                select(RoloReport)
            ).all()