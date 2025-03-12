import { useState } from "react";
import { Dialog, DialogContent, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function FormDirecao({ open, handleClose }) {
  const [direcao, setDirecao] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Direção:", direcao);
    handleClose();
  };

  return (
    <Dialog open={open} onOpenChange={handleClose}>
      <DialogContent>
        <DialogTitle>Cadastro de Direção</DialogTitle>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <Label htmlFor="direcao">Direção</Label>
            <Input
              id="direcao"
              type="text"
              value={direcao}
              onChange={(e) => setDirecao(e.target.value)}
              placeholder="Digite a direção..."
              required
            />
          </div>
          <div className="flex justify-end space-x-2">
            <Button type="button" variant="outline" onClick={handleClose}>
              Cancelar
            </Button>
            <Button type="submit">Salvar</Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}
