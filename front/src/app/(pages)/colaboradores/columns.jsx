"use client";

import { ArrowUpDown } from "lucide-react";
import { ColumnDef } from "@tanstack/react-table";
import { Button } from "@/components/ui/button";


export const columns = [
  {
    accessorKey: "nome",
    header: "Nome",
    filter: "text",
  },
  {
    accessorKey: "matricula",
    header: "Matrícula",
    filter: "text",
  },
  {
    accessorKey: "cpf",
    header: "CPF",
    filter: "text",
  },
  {
    accessorKey: "status",
    header: "Status",
  },
  {
    accessorKey: "telefone",
    header: "Telefone",
    filter: "text",
  },
  {
    accessorKey: "email",
    header: "Email",
    filter: "text",
  },
  {
    accessorKey: "direcao",
    header: "Direção",
  },
  {
    accessorKey: "gerencia",
    header: "Gerência",
  },
  {
    accessorKey: "coordenacao",
    header: "Coordenação",
  },
  {
    accessorKey: "criadoEm",
    header: "Criado em",
  },
  {
    accessorKey: "criadoPor",
    header: "Criado por",
  },
  {
    accessorKey: "atualizadoEm",
    header: "Atualizado em",
  },
  {
    accessorKey: "atualizadoPor",
    header: "Atualizado por",
  },
];

