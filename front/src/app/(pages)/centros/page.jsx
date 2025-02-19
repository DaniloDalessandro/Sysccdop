"use client";

import { DataTable } from "@/components/core/table/data-table";
import { columns } from "./columns";

const data = [
  {
    id: "1",
    nome: "Nome 1",
    criadoEm: "2023-01-01",
    criadoPor: "User 1",
    atualizadoEm: "2023-01-02",
    atualizadoPor: "User 2",
    status: "Ativo",
  },
  {
    id: "2",
    nome: "Nome 2",
    criadoEm: "2023-02-01",
    criadoPor: "User 3",
    atualizadoEm: "2023-02-02",
    atualizadoPor: "User 4",
    status: "Inativo",
  },
  {
    id: "3",
    nome: "Nome 3",
    criadoEm: "2023-03-01",
    criadoPor: "User 5",
    atualizadoEm: "2023-03-02",
    atualizadoPor: "User 6",
    status: "Ativo",
  },
  {
    id: "4",
    nome: "Nome 4",
    criadoEm: "2023-04-01",
    criadoPor: "User 7",
    atualizadoEm: "2023-04-02",
    atualizadoPor: "User 8",
    status: "Inativo",
  },
  {
    id: "5",
    nome: "Nome 5",
    criadoEm: "2023-05-01",
    criadoPor: "User 9",
    atualizadoEm: "2023-05-02",
    atualizadoPor: "User 10",
    status: "Ativo",
  },
  {
    id: "6",
    nome: "Nome 6",
    criadoEm: "2023-06-01",
    criadoPor: "User 11",
    atualizadoEm: "2023-06-02",
    atualizadoPor: "User 12",
    status: "Inativo",
  },
  {
    id: "7",
    nome: "Nome 7",
    criadoEm: "2023-07-01",
    criadoPor: "User 13",
    atualizadoEm: "2023-07-02",
    atualizadoPor: "User 14",
    status: "Ativo",
  },
  {
    id: "8",
    nome: "Nome 8",
    criadoEm: "2023-08-01",
    criadoPor: "User 15",
    atualizadoEm: "2023-08-02",
    atualizadoPor: "User 16",
    status: "Inativo",
  },
  {
    id: "9",
    nome: "Nome 9",
    criadoEm: "2023-09-01",
    criadoPor: "User 17",
    atualizadoEm: "2023-09-02",
    atualizadoPor: "User 18",
    status: "Ativo",
  },
  {
    id: "10",
    nome: "Nome 10",
    criadoEm: "2023-10-01",
    criadoPor: "User 19",
    atualizadoEm: "2023-10-02",
    atualizadoPor: "User 20",
    status: "Inativo",
  },
];

export default function Home() {
  const handleAdd = () => {
    alert("Adicionar novo item!");
  };

  return (
    <div className="container mx-auto py-1 px-2">
      
      <div className="space-y-2">
        <DataTable
          columns={columns}
          data={data}
          onAdd={handleAdd}
          title="Centro de Custo Gestor"                 
          pageSize={5}
        />
        <DataTable
          columns={columns}
          data={data}
          onAdd={handleAdd}
          title="Centro de Custo Solicitante"
          pageSize={5}
        />
      </div>
    </div>
  );
}