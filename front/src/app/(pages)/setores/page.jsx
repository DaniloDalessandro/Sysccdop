"use client";

import { useState } from "react";
import { DataTable } from "@/components/core/table/data-table";
import { columns } from "./columns";
import FormDirecao from "./formDirecao";
import FormGerencia from "./formGerencia";
import FormCoordenacao from "./formCoordenacao";

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
  const [openDirecao, setOpenDirecao] = useState(false);
  const [openGerencia, setOpenGerencia] = useState(false);
  const [openCoordenacao, setOpenCoordenacao] = useState(false);

  const handleOpen = (setOpen) => () => setOpen(true);
  const handleClose = (setOpen) => () => setOpen(false);

  return (
    <div className="container mx-auto py-1 px-2">
      <FormDirecao open={openDirecao} handleClose={handleClose(setOpenDirecao)} />
      <FormGerencia open={openGerencia} handleClose={handleClose(setOpenGerencia)} />
      <FormCoordenacao open={openCoordenacao} handleClose={handleClose(setOpenCoordenacao)} />

      <div className="space-y-2">
        <DataTable
          columns={columns}
          data={data}
          onAdd={handleOpen(setOpenDirecao)}
          title="Direção"
          pageSize={3}
        />
        <DataTable
          columns={columns}
          data={data}
          onAdd={handleOpen(setOpenGerencia)}
          title="Gerência"
          pageSize={3}
        />
        <DataTable
          columns={columns}
          data={data}
          onAdd={handleOpen(setOpenCoordenacao)}
          title="Coordenação"
          pageSize={3}
        />
      </div>
    </div>
  );
}
