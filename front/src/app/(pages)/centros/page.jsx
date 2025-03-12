"use client";

import { useState } from "react";
import { DataTable } from "@/components/core/table/data-table";
import { columns as columnsSolicitante } from "./columnsolicitante";
import { columns as columnsGestor } from "./columnsgestor";
import Formgestor from "./formgestor";
import Formsolicitante from "./formsolicitante";

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
];

export default function Home() {
  const [openGestor, setOpenGestor] = useState(false);
  const [openSolicitante, setOpenSolicitante] = useState(false);

  const handleAddGestor = () => setOpenGestor(true);
  const handleAddSolicitante = () => setOpenSolicitante(true);
  const handleCloseGestor = () => setOpenGestor(false);
  const handleCloseSolicitante = () => setOpenSolicitante(false);

  return (
    <div className="container mx-auto py-1 px-2">
      <Formgestor open={openGestor} handleClose={handleCloseGestor} />
      <Formsolicitante open={openSolicitante} handleClose={handleCloseSolicitante} />

      <div className="space-y-4">
        <DataTable
          columns={columnsGestor}
          data={data}
          onAdd={handleAddGestor}
          title="Centro de Custo Gestor"
          pageSize={5}
        />

        <DataTable
          columns={columnsSolicitante}
          data={data}
          onAdd={handleAddSolicitante}
          title="Centro de Custo Solicitante"
          pageSize={5}
        />
      </div>
    </div>
  );
}
