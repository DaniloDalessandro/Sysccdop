"use client";

import { DataTable } from "@/components/core/table/data-table";
import { columns } from "@/app/(pages)/centros/columns";

const data = [
  { status: "Active", email: "user1@example.com", amount: 100 },
  { status: "Inactive", email: "user2@example.com", amount: 200 },
];

export default function CentrosPage() {
  return (
    <div className="container mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Centros</h1>
      <DataTable columns={columns} data={data} />
    </div>
  );
}
