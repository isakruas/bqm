import requests


class TestUsuario:
    headers = {'Authorization': 'Token a_eddf5b0b978573f75365638fc6841fae745a8cef'}
    url = 'http://localhost:8000/api/v1/usuario/'

    """
        def test_get_usuarios(self):
            usuarios = requests.get(url=self.url, headers=self.headers)
    
            assert usuarios.status_code == 200
    
        def test_get_usuario(self):
            usuario = requests.get(url=f'{self.url}1/', headers=self.headers)
    
            assert usuario.status_code == 200
    """

    def test_post_usuario(self):
        data = {
            "email": "c@gmail.com",
            "password": "password",
            "nome": "nome",
            "sobrenome": "sobrenome",
            "escolaridade": "escolaridade",
            "nivel_de_acesso": "alfa"
        }
        usuario = requests.post(url=self.url, data=data)

        assert usuario.status_code == 201

    """
        def test_put_usuario(self):
            data = {
                "nome": "nome",
            }
            usuario = requests.put(url=f'{self.url}13/', headers=self.headers, data=data)
    
            assert usuario.status_code == 200
    
        def test_delete_usuario(self):
            usuario = requests.delete(url=f'{self.url}13/', headers=self.headers)
    
            assert usuario.status_code == 204 and len(usuario.text) == 0
    """