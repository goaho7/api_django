from rest_framework import serializers

from capibara.models import Statement


class StatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statement
        fields = '__all__'

    def validate_capibara_phrases(self, value):
        """ Удаление дублей """

        phrases = []
        [phrases.append(phrase) for phrase in value if phrase not in phrases]

        return phrases
