import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Select, SelectTrigger, SelectContent, SelectItem } from "@/components/ui/select"; // Importação do SelectContent
import { Textarea } from "@/components/ui/textarea";
import { assistanceSchema } from "./validations";

export default function AssistanceForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(assistanceSchema),
  });

  const onSubmit = (data) => {
    console.log("Dados enviados:", data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <Input placeholder="Funcionário" {...register("employee")} />
      {errors.employee && <p className="text-red-500">{errors.employee.message}</p>}
      
      <Input placeholder="Linha Orçamentária" {...register("budget_line")} />
      {errors.budget_line && <p className="text-red-500">{errors.budget_line.message}</p>}
      
      <Select {...register("type")}>
        <SelectTrigger>
          <Input placeholder="Tipo de Auxílio" /> {/* Exemplo de trigger */}
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="GRADUACAO">Graduação</SelectItem>
          <SelectItem value="POS_GRADUACAO">Pós-Graduação</SelectItem>
          <SelectItem value="AUXILIO_CHECHE_ESCOLA">Auxílio Creche Escola</SelectItem>
          <SelectItem value="LINGUA_ESTRANGEIRA">Língua Estrangeira</SelectItem>
        </SelectContent>
      </Select>
      {errors.type && <p className="text-red-500">{errors.type.message}</p>}
      
      <Input type="number" placeholder="Valor Total" {...register("total_amount", { valueAsNumber: true })} />
      {errors.total_amount && <p className="text-red-500">{errors.total_amount.message}</p>}
      
      <Input type="number" placeholder="Número de Parcelas" {...register("installment_count", { valueAsNumber: true })} />
      <Input type="number" placeholder="Valor por Parcela" {...register("amount_per_installment", { valueAsNumber: true })} />
      
      <Input type="date" placeholder="Data de Início" {...register("start_date")} />
      {errors.start_date && <p className="text-red-500">{errors.start_date.message}</p>}
      
      <Input type="date" placeholder="Data de Término" {...register("end_date")} />
      
      <Textarea placeholder="Observações" {...register("notes")} />
      
      <Select {...register("status")}>
        <SelectTrigger>
          <Input placeholder="Status" /> {/* Exemplo de trigger */}
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="AGUARDANDO">Aguardando Início</SelectItem>
          <SelectItem value="ATIVO">Ativo</SelectItem>
          <SelectItem value="CONCLUIDO">Concluído</SelectItem>
          <SelectItem value="CANCELADO">Cancelado</SelectItem>
        </SelectContent>
      </Select>
      {errors.status && <p className="text-red-500">{errors.status.message}</p>}
      
      <Button type="submit">Salvar</Button>
    </form>
  );
}
