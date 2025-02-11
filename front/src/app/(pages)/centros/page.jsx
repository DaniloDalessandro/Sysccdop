import { DataTable } from "@/components/core/data-table";
import { DataTableDemo } from "./table";

export default () => {

    const columns = [{id: 'id', label: 'ID'}, {id: 'amount', label: 'Amount'}, {id: 'status', label: 'Status'}, {id: 'email', label: 'Email'}]
    const data = [
        {
            id: '1',
            amount: 100,
            status: 'success',
            email: ''
        }]
    return (
        <div>
        <h1>Centros</h1>
        <DataTable title='Gestor' columns={columns} data={data}/>
        <DataTableDemo title='Gestor'/>

        <DataTableDemo title='Solicitante'/>

        
        </div>
    );
}