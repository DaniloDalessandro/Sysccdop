import { Plus } from "lucide-react"
import { Button } from "../ui/button"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "../ui/table"

export const DataTable = ({ title, columns = [],data=[] }) => {
    return (
        <div className="w-full">
            <div className="flex items-center py-4 justify-between">
                {title}
                <div>
                    <Button variant="outline" className="ml-auto">
                        Add novo <Plus />
                    </Button>
                </div>
            </div>

            <Table>
                <TableHeader>

                    <TableRow >
                        {columns.map((col) => {
                            return (
                                <TableHead key={col.id}>
                                    {col.label}
                                </TableHead>
                            )
                        })}
                    </TableRow>

                </TableHeader>
                <TableBody>
                        {data.map((row) => {
                            return (
                                <TableRow key={row.id}>
                                    {columns.map((col) => {
                                        return (
                                            <TableCell key={col.id}>
                                                {row[col.id]}
                                            </TableCell>
                                        )
                                    })}
                                </TableRow>
                            )
                        })}
                </TableBody>
            </Table>

        </div>
    )
}