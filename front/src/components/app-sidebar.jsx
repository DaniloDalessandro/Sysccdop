"use client"

import { BarChart, FileText, Users, Grid, User,HandHeart,DollarSign } from "lucide-react";
import * as React from "react"
import {
  AudioWaveform,
  BookOpen,
  Bot,
  Command,
  Frame,
  GalleryVerticalEnd,
  Map,
  PieChart,
  Settings2,
  SquareTerminal,
} from "lucide-react"

import { NavMain } from "@/components/nav-main"
import { NavProjects } from "@/components/nav-projects"
import { NavUser } from "@/components/nav-user"
import { TeamSwitcher } from "@/components/team-switcher"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarRail,
} from "@/components/ui/sidebar"


const data = {
  user: {
    name: "Danilo Costa",
    email: "danilodalessandro08@example.com",
    avatar: "/avatars/shadcn.jpg",
  },
  teams: [
    {
      name: "Minerva Contratos",
      logo: FileText,
      plan: "Emap",
    },
    {
      name: "Acme Corp.",
      logo: AudioWaveform,
      plan: "Startup",
    },
    {
      name: "Evil Corp.",
      logo: Command,
      plan: "Free",
    },
  ],
  navMain: [
    {
      title: "Dashboard",
      url: "/",
      icon: BarChart,
      isActive: true,
      
    },
    {
      title: "Contratos",
      url: "/",
      icon: FileText,
      isActive: true,
      
    },
    {
      title: "Auxílios",
      url: "/auxilios",
      icon: HandHeart,
      isActive: true,
      
    },
    {
      title: "Centros",
      url: "/centros",
      icon: Users,
      
    },
    {
      title: "Setores",
      url: "/setores",
      icon: Grid,
      
    },
    {
      title: "Colaboradores",
      url: "/colaboradores",
      icon: User,
      
    },
    {
      title: "Orçamentos",
      url: "/colaboradores",
      icon: DollarSign,
      
    },
    {
      title: "Linhas Orçamentarias",
      url: "/colaboradores",
      icon: User,
      
    },
  ]
}

export function AppSidebar({
  ...props
}) {
  return (
    (<Sidebar collapsible="icon" {...props}>
      <SidebarHeader>
        <TeamSwitcher teams={data.teams} />
      </SidebarHeader>
      <SidebarContent>
        <NavMain items={data.navMain} />
      </SidebarContent>
      <SidebarFooter>
        <NavUser user={data.user} />
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>)
  );
}
