from .models import Sellable


class Sellable_service:
    #model = Sellable

    def mark_sellable_as_reserved(self, id: str):
        sellable = Sellable.objects.get(pk=id)

        # Update the 'active' field
        sellable.is_Reserved = True
        sellable.save(update_fields=['is_Reserved'])
        return sellable

    def mark_sellable_as_bought(self, id: str):
        sellable = Sellable.objects.get(pk=id)

        # Update the 'active' field
        sellable.is_bought = True
        sellable.save(update_fields=['is_bought'])
        return sellable