from sqlalchemy import Column, String
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy_utils.types.uuid import UUIDType

from kommon.db import BaseModel
from kommon.choices import Choices

from kode.codecommit import CodeCommitClient

ISSUE_STATUS = Choices(("closed", "closed"), ("open", "open"))


class RepositoryModel(BaseModel):  # noqa
    """
    Campos do banco
    """

    repository_uid = None
    name = None
    text = None
    status = None

    def __init__(self):
        self.client = CodeCommitClient()

    def _fetch(self):
        """
        Gets, adds or updates repository from AWS Code Commit
        """
        # Retorna as informações da AWS e insere no banco
        try:
            response = self.client.get_repository(self.name)
        except self.client.exceptions.RepositoryDoesNotExistException:
            print("Não existe este repositorio")

        # Salva informações no banco

        # Retorna model salvo

        pass

    def exists():
        """
        Check if exists, returns true or flase
        """

        pass

    def get():
        """
        Get information from database
        """
        pass


class IssueModel(BaseModel):  # noqa
    repository_uid = Column(UUIDType(binary=False), unique=True)
    name = Column(String)
    text = Column(String)
    status = Column(ChoiceType(ISSUE_STATUS))

    """
    1) Check if repository exists - Nilton
    2) Get repository info (from AWS) - Nilton
    3) Create new issue - Luiz
        - Must check if repository exists before creating
        - Must validate
        - Must return itself
    4) Change issues status (update) - Luiz
    """

    def create():
        pass

    def set_status():
        pass
