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

export default ({ open, handleClose }) => {
  return (
    <Dialog open={open} onOpenChange={handleClose}>
      <DialogContent className="max-w-md">
        <DialogHeader>
          <DialogTitle>Cadastro de Centro Gestor</DialogTitle>
        </DialogHeader>

        {/* Campo Centro Gestor */}
        <div className="grid gap-2 py-4">
          <Label htmlFor="centroGestor">Centro Gestor</Label>
          <Input id="centroGestor" maxLength={20} placeholder="Digite o centro gestor" className="w-full" />
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
