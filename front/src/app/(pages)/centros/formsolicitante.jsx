import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";

export default ({ open, handleClose }) => {
  return (
    <Dialog open={open} onOpenChange={handleClose}>
      <DialogContent className="max-w-md">
        <DialogHeader>
          <DialogTitle>Cadastro de Centro</DialogTitle>
        </DialogHeader>

        <div className="grid gap-4 py-4">
          {/* Centro Gestor (Select) */}
          <div className="grid gap-2">
            <Label htmlFor="centroGestor">Centro Gestor</Label>
            <Select>
              <SelectTrigger className="w-full">
                <SelectValue placeholder="Selecione um centro gestor" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="financeiro">Financeiro</SelectItem>
                <SelectItem value="operacional">Operacional</SelectItem>
                <SelectItem value="administrativo">Administrativo</SelectItem>
              </SelectContent>
            </Select>
          </div>

          {/* Centro Solicitante (Campo Livre) */}
          <div className="grid gap-2">
            <Label htmlFor="centroSolicitante">Centro Solicitante</Label>
            <Input id="centroSolicitante" maxLength={100} placeholder="Digite o centro solicitante" className="w-full" />
          </div>
        </div>

        <hr className="border-t border-gray-300 my-0" />

        {/* Rodapé com Botão Menor */}
        <DialogFooter>
          <Button type="submit" className="px-4 py-2 text-sm">Salvar</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
