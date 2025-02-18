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
  // Adicione mais dados aqui...
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