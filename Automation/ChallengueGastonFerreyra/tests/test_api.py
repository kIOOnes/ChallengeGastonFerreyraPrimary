import unittest
from unittest.mock import patch, Mock
from xml.etree.ElementTree import tostring

import pytest

from api.api_methods import post,get

class TestApi():
    @pytest.mark.parametrize("cod_producto_parametrized, status_code_parametrized, id_proceso_parametrized", [
        (1, 201, 10),
        ("invalid", 400, 0),
        (2,500,0)

    ])
    @patch('requests.post')
    def test_api_post_compra(self,mock_post, cod_producto_parametrized, status_code_parametrized, id_proceso_parametrized):
        # Configurar la respuesta mockeada
        mock_response = Mock()
        mock_response.status_code = status_code_parametrized
        mock_response.json.return_value = {
            "idProceso": id_proceso_parametrized,
            "cantidadErrores": 0,
            "cantidadOperacionesProcesadas": 0
        }
        mock_post.return_value = mock_response

        # Llamar a la función que utiliza la API
        body = {
            "codProducto": cod_producto_parametrized,
            "codTipoSolicitud": "V",
            "fechaPedido": "2024-09-16",
            "importe": 700000,
            "esTotal": False,
            "idFormaPago": "CB",
            "idPedido": "H7",
            "requiereAutorizacion": False,
            "origen": "OT"
        }

        response = post(url="http://localhost:6003/api/negocio/v10/insert-pedidos-list", body=body)

        # Verificar la respuesta
        assert response.status_code == status_code_parametrized
        assert response.json() == mock_response.json()

    @pytest.mark.parametrize("cod_producto_parametrized, status_code_parametrized, id_proceso_parametrized", [
        (1, 201, 10),
        ("invalid", 400, 0),
        (2,500,0)

    ])
    @patch('requests.post')
    def test_api_post_venta(self,mock_post, cod_producto_parametrized, status_code_parametrized, id_proceso_parametrized):
        # Configurar la respuesta mockeada
        mock_response = Mock()
        mock_response.status_code = status_code_parametrized
        mock_response.json.return_value = {
            "idProceso": id_proceso_parametrized,
            "cantidadErrores": 0,
            "cantidadOperacionesProcesadas": 0
        }
        mock_post.return_value = mock_response

        # Llamar a la función que utiliza la API
        body = {
            "codProducto": cod_producto_parametrized,
            "codTipoSolicitud": "C",
            "fechaPedido": "2024-09-16",
            "importe": 700000,
            "esTotal": False,
            "idFormaPago": "CB",
            "idPedido": "H7",
            "requiereAutorizacion": False,
            "origen": "OT"
        }

        response = post(url="http://localhost:6003/api/negocio/v10/insert-pedidos-list", body=body)

        # Verificar la respuesta
        assert response.status_code == status_code_parametrized
        assert response.json() == mock_response.json()


    @patch('requests.post')
    @patch('requests.get')
    def test_api_get(self, mock_get, mock_post):
        # Configurar la respuesta mockeada para POST
        mock_response_post = Mock()
        mock_response_post.status_code = 201
        mock_response_post.json.return_value = {
            "idProceso": 33,
            "cantidadErrores": 0,
            "cantidadOperacionesProcesadas": 0
        }
        mock_post.return_value = mock_response_post

        # Configurar la respuesta mockeada para GET
        mock_response_get = Mock()
        mock_response_get.status_code = 200
        mock_response_get.json.return_value = {
            "idProceso": 33,
            "cantidadErrores": 0,
            "cantidadOperacionesProcesadas": 0
        }
        mock_get.return_value = mock_response_get

        # Llamar a la función que utiliza la API
        body = {
            "codProducto": 439,
            "codTipoSolicitud": "RE",
            "fechaPedido": "2024-09-16",
            "importe": 700000,
            "esTotal": False,
            "idFormaPago": "CB",
            "idPedido": "H7",
            "requiereAutorizacion": False,
            "origen": "OT"
        }
        try:
            response_post = post(url="http://localhost:6003/api/negocio/v10/insert-pedidos-list", body=body)
            response_get = get(url="http://localhost:6003/api/negocio/v10/insert-pedidos-list/" + str(
            response_post.json().get("idProceso")))
            # Verificar la respuesta

            assert response_get.status_code == 200
            assert response_get.json() == mock_response_get.json()

            #self.assertEqual(response_get.status_code, 200)
            #self.assertEqual(response_get.json(), mock_response_get.json())

        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")

if __name__ == "__main__":
    unittest.main()
