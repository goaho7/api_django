import xlwt
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from capibara.models import Statement
from api.serializers import StatementSerializer


@api_view(['POST'])
def generate(request):
    serializer = StatementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_statement_by_id(request, id):
    statement = Statement.objects.filter(id=id).first()
    if statement:
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="statement.xls"'
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Statement')
        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Capibara Format')
        worksheet.write(0, 2, 'Capibara Slang')
        worksheet.write(0, 3, 'Capibara Phrases')
        worksheet.write(1, 0, statement.id)
        worksheet.write(1, 1, statement.capibara_format)
        worksheet.write(1, 2, statement.capibara_slang)
        worksheet.write(1, 3, ', '.join(statement.capibara_phrases))
        workbook.save(response)
        return response
    return Response({'status': 'not available'}, status=404)


@api_view(['GET'])
def get_statements_by_slang(request, slang):
    statements = Statement.objects.filter(capibara_slang=slang)
    if statements:
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="statements.xls"'
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Statements')
        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Capibara Format')
        worksheet.write(0, 2, 'Capibara Slang')
        worksheet.write(0, 3, 'Capibara Phrases')
        row = 1
        for statement in statements:
            worksheet.write(row, 0, statement.id)
            worksheet.write(row, 1, statement.capibara_format)
            worksheet.write(row, 2, statement.capibara_slang)
            worksheet.write(row, 3, ', '.join(statement.capibara_phrases))
            row += 1
        workbook.save(response)
        return response
    return Response({'status': 'not available'}, status=404)
