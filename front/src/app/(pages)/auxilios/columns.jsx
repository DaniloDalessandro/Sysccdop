"use client";

export const columns = [
  {
    accessorKey: "employee",
    header: "Funcionário",
    filter: 'text',
  },
  {
    accessorKey: "budget_line",
    header: "Linha Orçamentária",
  },
  {
    accessorKey: "type",
    header: "Tipo",
  },
  {
    accessorKey: "total_amount",
    header: "Valor Total",
  },
  {
    accessorKey: "installment_count",
    header: "Número de Parcelas",
  },
  {
    accessorKey: "amount_per_installment",
    header: "Valor por Parcela",
  },
  {
    accessorKey: "start_date",
    header: "Data de Início",
  },
  {
    accessorKey: "end_date",
    header: "Data de Término",
  },
  {
    accessorKey: "notes",
    header: "Observações",
  },
  {
    accessorKey: "status",
    header: "Status",
  },
];
