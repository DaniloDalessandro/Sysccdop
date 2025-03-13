"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { collaboratorSchema } from "./validations";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";

export default function CollaboratorForm({ open, handleClose }) {
  const {
    register,
    handleSubmit,
    setValue,
    watch,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(collaboratorSchema),
  });

  const onSubmit = (data) => {
    console.log("Dados enviados:", data);
    handleClose(); // Fecha o modal após envio
  };

  return (
    <Dialog open={open} onOpenChange={handleClose}>
      <DialogContent className="max-w-3xl">
        <DialogHeader>
          <DialogTitle>Cadastro de Colaboradores</DialogTitle>
        </DialogHeader>

        <form onSubmit={handleSubmit(onSubmit)} className="grid gap-6 py-4">
          {/* Nome Completo */}
          <div className="grid gap-2">
            <Label htmlFor="name">Nome Completo</Label>
            <Input id="name" {...register("name")} placeholder="John Doe" className="w-full" />
            {errors.name && <p className="text-red-500 text-sm">{errors.name.message}</p>}
          </div>

          {/* Matrícula, CPF e Status */}
          <div className="grid grid-cols-3 gap-4">
            <div className="grid gap-2">
              <Label htmlFor="matricula">Matrícula</Label>
              <Input id="matricula" {...register("matricula")} placeholder="0000" className="w-full" />
              {errors.matricula && <p className="text-red-500 text-sm">{errors.matricula.message}</p>}
            </div>
            <div className="grid gap-2">
              <Label htmlFor="cpf">CPF</Label>
              <Input id="cpf" {...register("cpf")} placeholder="000.000.000-00" className="w-full" maxLengt={11}/>
              {errors.cpf && <p className="text-red-500 text-sm">{errors.cpf.message}</p>}
            </div>
            <div className="grid gap-2">
              <Label htmlFor="status">Status</Label>
              <Select onValueChange={(value) => setValue("status", value)}>
                <SelectTrigger className="w-full">
                  <SelectValue placeholder="Selecione" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="ativo">Ativo</SelectItem>
                  <SelectItem value="inativo">Inativo</SelectItem>
                </SelectContent>
              </Select>
              {errors.status && <p className="text-red-500 text-sm">{errors.status.message}</p>}
            </div>
          </div>

          {/* Telefone e Email */}
          <div className="grid grid-cols-2 gap-4">
            <div className="grid gap-2">
              <Label htmlFor="telefone">Telefone</Label>
              <Input id="telefone" {...register("telefone")} placeholder="(99) 99999-9999" className="w-full" />
              {errors.telefone && <p className="text-red-500 text-sm">{errors.telefone.message}</p>}
            </div>
            <div className="grid gap-2">
              <Label htmlFor="email">Email</Label>
              <Input id="email" {...register("email")} placeholder="john@email.com" className="w-full" />
              {errors.email && <p className="text-red-500 text-sm">{errors.email.message}</p>}
            </div>
          </div>

          {/* Direção, Gerência e Coordenação */}
          <div className="grid grid-cols-3 gap-4">
            <div className="grid gap-2">
              <Label htmlFor="direcao">Direção</Label>
              <Select onValueChange={(value) => setValue("direcao", value)}>
                <SelectTrigger className="w-full">
                  <SelectValue placeholder="Selecione" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="norte">Norte</SelectItem>
                  <SelectItem value="sul">Sul</SelectItem>
                  <SelectItem value="leste">Leste</SelectItem>
                  <SelectItem value="oeste">Oeste</SelectItem>
                </SelectContent>
              </Select>
              {errors.direcao && <p className="text-red-500 text-sm">{errors.direcao.message}</p>}
            </div>
            <div className="grid gap-2">
              <Label htmlFor="gerencia">Gerência</Label>
              <Select onValueChange={(value) => setValue("gerencia", value)}>
                <SelectTrigger className="w-full">
                  <SelectValue placeholder="Selecione" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="norte">Norte</SelectItem>
                  <SelectItem value="sul">Sul</SelectItem>
                  <SelectItem value="leste">Leste</SelectItem>
                  <SelectItem value="oeste">Oeste</SelectItem>
                </SelectContent>
              </Select>
              {errors.gerencia && <p className="text-red-500 text-sm">{errors.gerencia.message}</p>}
            </div>
            <div className="grid gap-2">
              <Label htmlFor="coordenacao">Coordenação</Label>
              <Select onValueChange={(value) => setValue("coordenacao", value)}>
                <SelectTrigger className="w-full">
                  <SelectValue placeholder="Selecione" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="norte">Norte</SelectItem>
                  <SelectItem value="sul">Sul</SelectItem>
                  <SelectItem value="leste">Leste</SelectItem>
                  <SelectItem value="oeste">Oeste</SelectItem>
                </SelectContent>
              </Select>
              {errors.coordenacao && <p className="text-red-500 text-sm">{errors.coordenacao.message}</p>}
            </div>
          </div>

          {/* Rodapé */}
          <DialogFooter className="flex justify-between">
            <Button type="button" onClick={handleClose} className="px-4 py-2 text-sm"> Cancelar </Button>
            <Button type="submit" className="px-4 py-2 text-sm">Salvar</Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
