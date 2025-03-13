import { z } from "zod";

export const collaboratorSchema = z.object({
  name: z.string().min(3, "Nome deve ter pelo menos 3 caracteres").max(100, "Máximo de 100 caracteres"),
  matricula: z.string().min(4, "Matrícula deve ter 4 dígitos").max(4, "Matrícula deve ter 4 dígitos"),
  cpf: z.string().regex(/^\d{11}$/, "CPF deve conter exatamente 11 números").max(11, "CPF deve conter exatamente 11 números"),
  status: z.enum(["ativo", "inativo"], { message: "Selecione um status válido" }),
  telefone: z.string().min(10, "Telefone inválido").max(11, "Telefone inválido"),
  email: z.string().email("E-mail inválido"),
  direcao: z.enum(["norte", "sul", "leste", "oeste"], { message: "Selecione uma direção" }),
  gerencia: z.enum(["norte", "sul", "leste", "oeste"], { message: "Selecione uma gerência" }),
  coordenacao: z.enum(["norte", "sul", "leste", "oeste"], { message: "Selecione uma coordenação" }),
});
