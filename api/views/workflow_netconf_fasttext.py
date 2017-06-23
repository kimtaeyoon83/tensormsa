import json
from rest_framework.response import Response
from rest_framework.views import APIView
from master.workflow.netconf.workflow_netconf_fasttext import WorkFlowNetConfFastText as ft_conf

class WorkFlowNetConfFastText(APIView):
    """
    """
    def post(self, request, nnid, ver, node):
        """
        - desc : insert configuration data
        """
        try:
            key = ''.join([nnid, '_' , ver, '_' , node])
            return_data = ft_conf(key).set_conf_data(request.data)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, nnid, ver, node):
        """
        - desc : get configuration data
        """
        try:
            key = ''.join([nnid, '_', ver, '_', node])
            return_data = ft_conf(key).get_conf_data(request.data)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, nnid, ver, node):
        """
        - desc ; update config data
        """
        try:
            key = ''.join([nnid, '_', ver, '_', node])
            return_data = ft_conf(key).set_conf_data(request.data)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, nnid, ver, node):
        """
        - desc : delete cnn configuration data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))
