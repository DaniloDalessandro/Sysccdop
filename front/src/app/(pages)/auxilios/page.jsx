"use client";

import { useState } from "react";
import { DataTable } from "@/components/core/table/data-table";
import { columns as assistanceColumns } from "./columns"; // Verifique se as colunas estão importadas corretamente
import AssistanceForm from "./form"; // Importação do formulário de assistência

// Dados de exemplo para a tabela
const data = [
  {
    id: "1",
    employee: "João Silva",
    budget_line: "Orçamento 2023",
    type: "GRADUACAO",
    total_amount: 5000,
    installment_count: 10,
    amount_per_installment: 500,
    start_date: "2023-01-01",
    end_date: "2023-10-01",
    notes: "Auxílio para graduação",
    status: "ATIVO",
  },
  {
    id: "2",
    employee: "Maria Souza",
    budget_line: "Orçamento 2024",
    type: "POS_GRADUACAO",
    total_amount: 8000,
    installment_count: 8,
    amount_per_installment: 1000,
    start_date: "2024-02-01",
    end_date: "2024-09-01",
    notes: "Auxílio para pós-graduação",
    status: "AGUARDANDO",
  },
];

export default function AssistancePage() {
  const [openForm, setOpenForm] = useState(false);

  // Função para abrir o formulário
  const handleAdd = () => setOpenForm(true);

  // Função para fechar o formulário
  const handleClose = () => setOpenForm(false);

  return (
    <div className="container mx-auto py-4 px-6">
      {/* Modal de formulário de assistência */}
      {openForm && (
        <div className="fixed inset-0 flex justify-center items-center z-50 bg-black bg-opacity-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-full sm:w-96">
            <AssistanceForm open={openForm} handleClose={handleClose} />
          </div>
        </div>
      )}

      <div className="space-y-4">
        {/* DataTable para exibir os dados de assistência */}
        <DataTable
          columns={assistanceColumns} // As colunas da tabela, definidas em './columns'
          data={data} // Dados que serão exibidos na tabela
          onAdd={handleAdd} // Função que abre o formulário de novo item
          title="Assistências"
          pageSize={5} // Número de registros por página
        />
      </div>
    </div>
  );
}
