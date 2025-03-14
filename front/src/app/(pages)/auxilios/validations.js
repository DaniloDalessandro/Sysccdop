import * as z from "zod";

export const assistanceSchema = z.object({
  employee: z.string().min(1, "Funcionário é obrigatório"),
  budget_line: z.string().min(1, "Linha Orçamentária é obrigatória"),
  type: z.enum([
    "GRADUACAO",
    "POS_GRADUACAO",
    "AUXILIO_CHECHE_ESCOLA",
    "LINGUA_ESTRANGEIRA",
  ]),
  total_amount: z.number().min(0.01, "Valor total deve ser maior que 0"),
  installment_count: z.number().optional(),
  amount_per_installment: z.number().optional(),
  start_date: z.string().min(1, "Data de Início é obrigatória"),
  end_date: z.string().optional(),
  notes: z.string().optional(),
  status: z.enum(["AGUARDANDO", "ATIVO", "CONCLUIDO", "CANCELADO"]),
});
