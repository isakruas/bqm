from rest_framework import permissions


class FiliacaoPermissions(permissions.BasePermission):
    niveis = ('admin', 'alfa', 'beta', 'gama', 'delta')

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        nivel = request.user.nivel_de_acesso
        if nivel in self.niveis:
            # se for administrador aceitar conexao
            return True
        else:
            return False


class ImprimirPermissions(permissions.BasePermission):
    methods = ('POST', 'PUT', 'PATCH', 'DELETE')
    niveis = ('admin', 'alfa', 'beta', 'gama', 'delta')

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        nivel = request.user.nivel_de_acesso
        if nivel in self.niveis:
            # se for administrador aceitar conexao
            return True

        elif request.method == 'POST':
            # se não for adm, verificar metodos
            if request.data:
                if 'cadastro_pelo_usuario' in request.data:
                    id_request = request.data['cadastro_pelo_usuario']
                    user = request.user
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


class UsuarioPermissions(permissions.BasePermission):
    methods = ('POST',)
    niveis = ('admin', 'alfa', 'beta', 'gama', 'delta')

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if request.method in self.methods:
                return True
            else:
                return False
        else:
            nivel = request.user.nivel_de_acesso
            if nivel in self.niveis:
                return True
            else:
                uid = request.user.id
                path = request.META['PATH_INFO']
                if str(uid) in str(path):
                    return True
                else:
                    return False

    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated:
            return False

        user = request.user

        if int(user.id) == int(obj.id):
            """
                Se o obj for dele, liberar tudo
            """
            return True
        else:
            """
                Se o objeto nao for dele, verificar se
                é um administrador
            """
            nivel = user.nivel_de_acesso
            if nivel in self.niveis:
                """
                    Se for administrador, liberar acesso
                    caso contrario, negar
                """
                return True
            else:

                return False
