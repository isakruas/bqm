from rest_framework import permissions

"""
    Permite que o usuario leia as questoes
    Permite que o usuario só possa alterar as questoes que forem suas
    com execao dos usuarios administradores
"""


class UsuarioPermissions(permissions.BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        nivel = request.user.nivel_de_acesso

        if request.method == 'POST':
            if (
                    nivel == 'admin' or
                    nivel == 'alfa' or
                    nivel == 'beta'
            ):
                return True
            else:
                return False
        else:
            return True

    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated:
            return False

        if request.method == 'GET':
            return True

        nivel = request.user.nivel_de_acesso

        if (
                nivel == 'admin' or
                nivel == 'alfa' or
                nivel == 'beta'
        ):
            return True
        else:
            return False


class QuestaoPermissions(permissions.BasePermission):
    niveis = ('admin', 'alfa', 'beta', 'gama', 'delta')

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.method == 'POST':
            if request.data:
                user = request.user
                if str(request.user.nivel_de_acesso) in self.niveis:
                    return True
                if 'cadastro_pelo_usuario' in request.data:
                    id_request = request.data['cadastro_pelo_usuario']
                    if int(id_request) == int(user.id):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return True
        else:
            return True

    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated:
            return False

        user = request.user
        nivel = user.nivel_de_acesso

        if request.method == 'GET':
            return True

        if request.method == 'PUT':
            if str(user.email) == str(obj.cadastro_pelo_usuario):
                return True
            elif (
                    nivel == 'admin' or
                    nivel == 'alfa' or
                    nivel == 'beta' or
                    nivel == 'gama' or
                    nivel == 'delta'
            ):
                return True
            else:
                return False

        if request.method == 'PATCH':
            if str(user.email) == str(obj.cadastro_pelo_usuario):
                return True
            elif (
                    nivel == 'admin' or
                    nivel == 'alfa' or
                    nivel == 'beta' or
                    nivel == 'gama' or
                    nivel == 'delta'
            ):
                return True
            else:
                return False

        if request.method == 'DELETE':
            if str(user.email) == str(obj.cadastro_pelo_usuario):
                return True
            elif (
                    nivel == 'admin' or
                    nivel == 'alfa' or
                    nivel == 'beta' or
                    nivel == 'gama' or
                    nivel == 'delta'
            ):
                return True
            else:
                return False
