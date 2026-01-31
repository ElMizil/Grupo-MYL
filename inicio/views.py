from django.views.generic import TemplateView
from django.utils import timezone
from django.db.models import Sum, Count, Avg
from datetime import timedelta

# Ajusta el import a tu modelo real:
# from diesel.models import DieselLog

class DashboardView(TemplateView):
    template_name = "inicio/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # Rango default (últimos 30 días)
        today = timezone.localdate()
        start = today - timedelta(days=30)

        # Ejemplo base: si tienes DieselLog con fields litros, total_cost, created_at, unidad, ubicacion
        # qs = DieselLog.objects.filter(created_at__date__gte=start, created_at__date__lte=today)

        # Si todavía no tienes el modelo listo, deja valores dummy:
        ctx["kpis"] = [
            {"label": "Recargas (30 días)", "value": 0},
            {"label": "Litros totales", "value": 0},
            {"label": "Costo total", "value": "$0.00"},
            {"label": "Promedio por recarga", "value": 0},
        ]

        # Cuando conectes el modelo, tu versión real sería algo así:
        # ctx["kpis"] = [
        #     {"label": "Recargas (30 días)", "value": qs.count()},
        #     {"label": "Litros totales", "value": qs.aggregate(v=Sum("litros"))["v"] or 0},
        #     {"label": "Costo total", "value": qs.aggregate(v=Sum("costo_total"))["v"] or 0},
        #     {"label": "Promedio por recarga", "value": qs.aggregate(v=Avg("litros"))["v"] or 0},
        # ]

        # Lugar para widgets (tablas, gráficas)
        ctx["widgets"] = {
            "recent_activity": [],
            "alerts": [],
        }

        return ctx
