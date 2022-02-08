from cgi import print_directory
from django.http import JsonResponse

# 返回结果
res = {
  "status": "",
  "data": "",
  "msg": "",
}

def init(request):
    print(request.method)
    if request.method == 'POST':
      return JsonResponse(res, content_type='application/json')
    else:
      res['data'] = 111
      return JsonResponse(res)
