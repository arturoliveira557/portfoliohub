"""Módulo principal do PortfolioHUB.

Este módulo contém funções simples e testáveis para validar projetos cadastrados
em um portfólio digital. Ele foi criado para demonstrar o fluxo SDD, decomposição
em unidades e harness de testes automatizados.
"""

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Projeto:
    """Representa um projeto exibido no PortfolioHUB."""

    titulo: str
    categoria: str
    url: str
    status: str = "publicado"


def validar_url(url: str) -> bool:
    """Valida se a URL usa protocolo seguro HTTP/HTTPS e possui domínio."""
    if not isinstance(url, str):
        return False
    url = url.strip()
    if not (url.startswith("https://") or url.startswith("http://")):
        return False
    dominio = url.split("//", 1)[1]
    return "." in dominio and len(dominio) >= 4


def validar_projeto(projeto: Projeto) -> bool:
    """Valida os campos obrigatórios de um projeto."""
    campos_texto = [projeto.titulo, projeto.categoria, projeto.status]
    if any(not isinstance(campo, str) or not campo.strip() for campo in campos_texto):
        return False
    return validar_url(projeto.url)


def listar_projetos_publicados(projetos: Iterable[Projeto]) -> List[Projeto]:
    """Retorna apenas projetos válidos com status publicado."""
    return [p for p in projetos if validar_projeto(p) and p.status.lower() == "publicado"]


def buscar_por_categoria(projetos: Iterable[Projeto], categoria: str) -> List[Projeto]:
    """Busca projetos publicados por categoria, ignorando maiúsculas/minúsculas."""
    if not categoria or not isinstance(categoria, str):
        return []
    categoria_normalizada = categoria.strip().lower()
    return [
        p for p in listar_projetos_publicados(projetos)
        if p.categoria.strip().lower() == categoria_normalizada
    ]


def total_por_categoria(projetos: Iterable[Projeto], categoria: str) -> int:
    """Conta quantos projetos publicados existem em uma categoria."""
    return len(buscar_por_categoria(projetos, categoria))
