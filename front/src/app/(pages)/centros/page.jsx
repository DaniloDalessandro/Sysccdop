"use client";

import { DataTable } from "@/components/core/table/data-table";
import { columns } from "./columns";

const data = [
  {
    id: "1",
    status: "Ativo",
    email: "exemplo1@email.com",
    amount: 100,
  },
  {
    id: "2",
    status: "Inativo",
    email: "exemplo2@email.com",
    amount: 200,
  },
  {
    id: "3",
    status: "Ativo",
    email: "exemplo3@email.com",
    amount: 150,
  },
  {
    id: "4",
    status: "Inativo",
    email: "exemplo4@email.com",
    amount: 300,
  },
  {
    id: "5",
    status: "Ativo",
    email: "exemplo5@email.com",
    amount: 250,
  },
  {
    id: "6",
    status: "Inativo",
    email: "exemplo6@email.com",
    amount: 400,
  },
  {
    id: "7",
    status: "Ativo",
    email: "exemplo7@email.com",
    amount: 500,
  },
  {
    id: "8",
    status: "Inativo",
    email: "exemplo8@email.com",
    amount: 600,
  },
  {
    id: "9",
    status: "Ativo",
    email: "exemplo9@email.com",
    amount: 350,
  },
  {
    id: "10",
    status: "Inativo",
    email: "exemplo10@email.com",
    amount: 450,
  },
];

export default function Home() {
  const handleAdd = () => {
    alert("Adicionar novo item!");
  };

  return (
    <div className="container mx-auto py-10">
      <DataTable
        columns={columns}
        data={data}
        onAdd={handleAdd}
        title="Centro de Custo Gestor"
      />
    </div>
  );
}