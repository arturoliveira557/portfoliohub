import pytest

from app.portfoliohub import (
    Projeto,
    buscar_por_categoria,
    listar_projetos_publicados,
    total_por_categoria,
    validar_projeto,
    validar_url,
)


def test_validar_url_segura_com_dominio():
    assert validar_url("https://arturoliveira557.github.io/portfoliohub/") is True


def test_validar_url_sem_protocolo_retorna_falso():
    assert validar_url("arturoliveira557.github.io/portfoliohub") is False


def test_validar_projeto_com_campos_obrigatorios():
    projeto = Projeto(
        titulo="PortfolioHUB",
        categoria="Portfólio",
        url="https://github.com/arturoliveira557/portfoliohub",
    )
    assert validar_projeto(projeto) is True


def test_validar_projeto_sem_titulo_retorna_falso():
    projeto = Projeto(titulo="", categoria="Portfólio", url="https://example.com")
    assert validar_projeto(projeto) is False


def test_listar_apenas_projetos_publicados_e_validos():
    projetos = [
        Projeto("PortfolioHUB", "Portfólio", "https://example.com/portfolio", "publicado"),
        Projeto("Projeto Interno", "Sistema", "https://example.com/interno", "rascunho"),
        Projeto("Projeto sem URL", "Sistema", "sem-url", "publicado"),
    ]
    publicados = listar_projetos_publicados(projetos)
    assert len(publicados) == 1
    assert publicados[0].titulo == "PortfolioHUB"


def test_buscar_por_categoria_ignora_maiusculas():
    projetos = [
        Projeto("PortfolioHUB", "Portfólio", "https://example.com/portfolio"),
        Projeto("Sistema de Vendas", "Banco de Dados", "https://example.com/vendas"),
    ]
    resultado = buscar_por_categoria(projetos, "portfólio")
    assert len(resultado) == 1
    assert resultado[0].titulo == "PortfolioHUB"


def test_total_por_categoria_sem_resultado():
    projetos = [Projeto("PortfolioHUB", "Portfólio", "https://example.com/portfolio")]
    assert total_por_categoria(projetos, "IA") == 0
