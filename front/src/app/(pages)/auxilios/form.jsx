"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { assistanceSchema } from "./validations";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";

export default function AssistanceForm({ open, handleClose }) {
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(assistanceSchema),
  });

  const onSubmit = (data) => {
    console.log("Dados enviados:", data);
    handleClose(); // Fecha o modal após o envio
  };

  return (
    <Dialog open={open} onOpenChange={handleClose}>
      <DialogContent className="max-w-2xl"> 
        <DialogHeader>
          <DialogTitle>Cadastro de Auxílio</DialogTitle>
        </DialogHeader>

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          {/* Funcionário */}
          <div className="grid gap-2">
            <Label htmlFor="employee">Funcionário</Label>
            <Input id="employee" {...register("employee")} placeholder="Nome do funcionário" className="w-full" />
            {errors.employee && <p className="text-red-500 text-sm">{errors.employee.message}</p>}
          </div>

          {/* Linha Orçamentária */}
          <div className="grid gap-2">
            <Label htmlFor="budget_line">Linha Orçamentária</Label>
            <Select onValueChange={(value) => setValue("type", value)}>
              <SelectTrigger className="w-full">
                <SelectValue placeholder="Selecione o tipo de auxílio" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="AAAAA">Graduação</SelectItem>
                <SelectItem value="BBBBB">Pós-Graduação</SelectItem>
                <SelectItem value="CCCCC">Auxílio Creche Escola</SelectItem>
                <SelectItem value="DDDDD">Língua Estrangeira</SelectItem>
              </SelectContent>
            </Select>
            {errors.budget_line && <p className="text-red-500 text-sm">{errors.budget_line.message}</p>}
          </div>

          {/* Tipo de Auxílio */}
          <div className="grid gap-2">
            <Label htmlFor="type">Tipo de Auxílio</Label>
            <Select onValueChange={(value) => setValue("type", value)}>
              <SelectTrigger className="w-full">
                <SelectValue placeholder="Selecione o tipo de auxílio" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="GRADUACAO">Graduação</SelectItem>
                <SelectItem value="POS_GRADUACAO">Pós-Graduação</SelectItem>
                <SelectItem value="AUXILIO_CHECHE_ESCOLA">Auxílio Creche Escola</SelectItem>
                <SelectItem value="LINGUA_ESTRANGEIRA">Língua Estrangeira</SelectItem>
              </SelectContent>
            </Select>
            {errors.type && <p className="text-red-500 text-sm">{errors.type.message}</p>}
          </div>

          {/* Valor Total, Número de Parcelas e Valor por Parcela */}
          <div className="grid grid-cols-3 gap-4">
            <div className="grid gap-2">
              <Label htmlFor="total_amount">Valor Total</Label>
              <Input
                id="total_amount"
                type="number"
                {...register("total_amount", { valueAsNumber: true })}
                placeholder="Valor total"
                className="w-full"
              />
              {errors.total_amount && <p className="text-red-500 text-sm">{errors.total_amount.message}</p>}
            </div>
            <div className="grid gap-2">
              <Label htmlFor="installment_count">Número de Parcelas</Label>
              <Input
                id="installment_count"
                type="number"
                {...register("installment_count", { valueAsNumber: true })}
                placeholder="Número de parcelas"
                className="w-full"
              />
              {errors.installment_count && <p className="text-red-500 text-sm">{errors.installment_count.message}</p>}
            </div>
            <div className="grid gap-2">
              <Label htmlFor="amount_per_installment">Valor por Parcela</Label>
              <Input
                id="amount_per_installment"
                type="number"
                {...register("amount_per_installment", { valueAsNumber: true })}
                placeholder="Valor por parcela"
                className="w-full"
              />
              {errors.amount_per_installment && <p className="text-red-500 text-sm">{errors.amount_per_installment.message}</p>}
            </div>
          </div>

          {/* Data de Início e Data de Término */}
          <div className="grid grid-cols-2 gap-4">
            <div className="grid gap-2">
              <Label htmlFor="start_date">Data de Início</Label>
              <Input id="start_date" type="date" {...register("start_date")} className="w-full" />
              {errors.start_date && <p className="text-red-500 text-sm">{errors.start_date.message}</p>}
            </div>
            <div className="grid gap-2">
              <Label htmlFor="end_date">Data de Término</Label>
              <Input id="end_date" type="date" {...register("end_date")} className="w-full" />
              {errors.end_date && <p className="text-red-500 text-sm">{errors.end_date.message}</p>}
            </div>
          </div>

          {/* Observações */}
          <div className="grid gap-2">
            <Label htmlFor="notes">Observações</Label>
            <Textarea id="notes" {...register("notes")} placeholder="Observações" className="w-full" />
            {errors.notes && <p className="text-red-500 text-sm">{errors.notes.message}</p>}
          </div>

          {/* Status */}
          <div className="grid gap-2">
            <Label htmlFor="status">Status</Label>
            <Select onValueChange={(value) => setValue("status", value)}>
              <SelectTrigger className="w-full">
                <SelectValue placeholder="Selecione o status" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="AGUARDANDO">Aguardando Início</SelectItem>
                <SelectItem value="ATIVO">Ativo</SelectItem>
                <SelectItem value="CONCLUIDO">Concluído</SelectItem>
                <SelectItem value="CANCELADO">Cancelado</SelectItem>
              </SelectContent>
            </Select>
            {errors.status && <p className="text-red-500 text-sm">{errors.status.message}</p>}
          </div>

          {/* Rodapé do Dialog */}
          <DialogFooter className="flex justify-between">
            <Button type="button" variant="outline" onClick={handleClose}>
              Cancelar
            </Button>
            <Button type="submit">Salvar</Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}