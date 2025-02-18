"use client";

import { ArrowUpDown } from "lucide-react";
import { ColumnDef } from "@tanstack/react-table";
import { Button } from "@/components/ui/button";

export const columns = [
  {
    accessorKey: "nome",
    header: "Nome",
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
  {
    accessorKey: "status",
    header: "Status",
  },
];
